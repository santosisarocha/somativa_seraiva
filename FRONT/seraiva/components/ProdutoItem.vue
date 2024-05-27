<script setup lang="ts">
import { type Livro } from '~/models/produtos';
import { carrinho } from "#imports";
import { computed } from "#imports";

const { adicionarNoCarrinho, getCarrinho, estaNoCarrinho } = carrinho();

type propType = {
    livro: Livro;
}

const props = defineProps<propType>();
const emit = defineEmits(['eventoAdicionado']); 

const adicionarItem = () => {
  if (props.livro.quantidade > 0) {
    adicionarNoCarrinho(props.livro);
    emit('eventoAdicionado');
    console.log("CARRINHO ATUAL: ", getCarrinho());
  }
}

const produtoNoCarrinho = computed(() => {
  return estaNoCarrinho(props.livro);   
});

const botaoLabel = computed(() => {
  return props.livro.quantidade > 0 ? "Adicionar" : "Indisponível";
});
</script>

<template>
    <div>
        <section class="cartao flex flex-column align-items-center justify-content-center" v-if="props.livro">
            <div class="produto-imagem">
                <img :src="props.livro.foto">
            </div>
            <div>
                <h4>{{ props.livro.titulo }}</h4>
            </div>
            <div class="flex flex-row">
                <span>R${{ props.livro.preco }} - </span>
                <div class="ml-2">
                    <label>Qtd. Disponivel: </label>
                    <span>{{ props.livro.quantidade }}</span>
                </div>                
            </div>
            <Rating v-model="props.livro.estrelas" readonly class="estrela" :cancel="false" />
            
            <Button @click="adicionarItem" class="botao-add" :label="botaoLabel" />
        </section>
    </div>
</template>

<style scoped lang="scss">
.cartao {
    width: 300px;
    max-width: 300px;
    height: 450px;
    max-height: 450px;
    background-color: rgba(255, 255, 255, 0.63);
    border-radius: 1.5rem;
    margin: 1.5rem;
    cursor: pointer;
    &:hover {
        transform: scale(1.1);
        transition: 1s;
    }

    .produto-imagem {
        width: 75%;
        height: 70%;
        max-width: 250px;
        max-height: 250px;
        img {
            margin-top: 15px;
            
            border-radius: 1.5rem;
            width: 100%;
            height: 100%;
        }
    }
    .botao-add {
        width: 70%;
        height: 4rem;
        margin: 1rem;
        background-color: rgb(18, 15, 41);
        border-color: rgb(18, 15, 41);
    }
    
}
</style>
