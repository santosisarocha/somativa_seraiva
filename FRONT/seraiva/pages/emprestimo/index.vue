<script setup lang="ts">
import { computed } from "#imports";
import { carrinho, type CarrinhoItem } from "#imports";
const { getCarrinho, removerDoCarinho, getValorTotalDoCarrinho, esvaziarCarrinho } = carrinho();
import { salvarVenda, salvarVendaProdutos } from "~/services/vendas";
const { data } = useAuth();
import type { EmprestimoLivroBody } from "~/models/vendas";
import { type Usuario } from "~/models/usuario";

definePageMeta({
  middleware: "auth",
});

const usuarioLogado = computed<Usuario | null>(() => {
  if (data.value && Array.isArray(data.value)) {
    return data.value.length > 0 ? data.value[0] as Usuario : null;
  }
  return null;
});


//pegando os itens que estão no carrinho e salvando
//na variavel
const itensNoCarrinho = computed<Array<CarrinhoItem>>(()=>getCarrinho());
const valorTotal = computed(() => getValorTotalDoCarrinho().toPrecision(5));

const carregando = ref(false);
const salvo = ref(false);

console.log("itens No carrinho.....", itensNoCarrinho);

const deletarDoCarrinho = (itemParaRemover: CarrinhoItem) => {
  removerDoCarinho({
    livro: itemParaRemover.livro,
    quantidade: 0
  });
}

const salvarPedido = () => {
  if (getCarrinho().length) {
    carregando.value = true;
    console.log("data", data.value)
    salvarVenda({
      usuarioFK: usuarioLogado.value ? `${usuarioLogado.value.id}` : ''
    }).then(vendaSalva => {
      console.log("venda salva: ", vendaSalva);
      let payload: Array<EmprestimoLivroBody> = [];
      getCarrinho().forEach(item => {
        payload.push({
          emprestimoFK: vendaSalva?.id ?? 0,
          livroFK: item.livro.id ?? 0,
          quantidade: item.quantidade,
        })
      });

      salvarVendaProdutos(payload).then(resposta => {
        console.log("ITENS DE VENDA SALVOS!", resposta);
        setTimeout(() => {
          salvo.value = true;
          
          esvaziarCarrinho();
        }, 3000);
      }).catch(error => {
        console.error("Erro ao salvar venda! ", error);
      });

    }).catch(error => {
      console.error("Erro ao salvar venda! ", error);
    })
      .finally(() => {
        setTimeout(() => {
          carregando.value = false;
        }, 3000);
      });
  }

}

</script>

<template>
  <main class="carrinho-container flex flex-column align-items-center">
    <h2 class="text" > Seu carrinho de compras</h2>
    <div class="card flex justify-content-center" v-if="carregando">
      <ProgressSpinner />
    </div>
    <table v-if="!carregando">
      <thead>
        <tr class="text-center">
          <td>Item</td>
          <td>Produto</td>
          <td>Descrição</td>
          <td>Categoria</td>
          <td>Preço Unitário</td>
          <td>Quantidade</td>
          <td>Subtotal</td>
          <td>Ações</td>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(itemCarrinho, index) in itensNoCarrinho" :key="index" class="text-center">
          <td>{{ index + 1 }}</td>
          <td><img class="fotoProduto" :src="itemCarrinho.livro.foto" alt="foto produto" /></td>
          <td>{{ itemCarrinho.livro.titulo }}</td>
          <td>{{ itemCarrinho.livro.categoriaFK.nome }}</td>
          <td>R$ {{ itemCarrinho.livro.preco }}</td>
          <td>{{ itemCarrinho.quantidade }}</td>
          <td>R$ {{ itemCarrinho.quantidade * itemCarrinho.livro.preco }}</td>
          <td>
            <Button @click="deletarDoCarrinho(itemCarrinho)" label=""><i class="pi pi-trash"></i></Button>
          </td>
        </tr>
      </tbody>
      <tfoot>
        <tr class="text-center">
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th>Valor Total:</th>
          <th>R${{ valorTotal }}</th>
        </tr>
      </tfoot>
    </table>
    <Button :disabled="salvo" v-if="!carregando" @click="salvarPedido" class="mt-2 botao-pedido" label="Fechar pedido" />
    <Message v-if="salvo" severity="success">
      <p>Pedido realizado com sucesso!</p>
      <p>Consulte seus itens em <NuxtLink to="/pedidos">Meus Pedidos</NuxtLink> </p>
    </Message>

  </main>
</template>

<style scoped lang="scss">
$largura-tabela: 90vw;

.carrinho-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: rgb(18, 15, 41);

  
  background-repeat: repeat;
  background-size: cover;
}
.text{
  color: aliceblue;
}

table {
  width: $largura-tabela;
  background-color: white;
  border-radius: 1rem;
}

thead {
  font-weight: bold;

  tr {
    border-bottom: 2px solid black
  }
}

td {
  padding: 1rem;
}

.fotoProduto {
  width: 70px;
  height: 70px;
}

Button {
  background-color: white;
  color: rgb(114, 15, 15);
  border: none;
}

.valor-total {
  font-weight: bold;
  width: 900px
}

.botao-pedido {
  width: 150px;
  height: 40px;
  background-color: #50ab9e ;
  color: aliceblue;

  &:hover {
    transform: scale(1.05);
    transition: 2s;
  }
}

</style>
