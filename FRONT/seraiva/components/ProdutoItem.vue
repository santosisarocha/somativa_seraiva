<script setup lang="ts">
import { type Livro } from '~/models/produtos';
type propType = {
    livro: Livro;
}

const props = defineProps<propType>();
console.log("produto recebido", props.livro);

</script>

<template>
    <div>
        <section class="cartao flex flex-column align-items-center justify-content-center"
        v-if="props.livro"
        >
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
            
            <Button class="botao-add" label="Adicionar"/>
            

        </section>

    </div>
</template>

<style scoped lang="scss">
    .cartao{
        width: 300px;
        max-width: 300px;
        height: 350px;
        max-height: 350px;
        background-color: rgba(255, 255, 255, 0.63);
        border-radius: 1.5rem;
        margin: 1.5rem;
        cursor: pointer;
        &:hover{
            transform: scale(1.1);
            transition: 1s;
        }

        .produto-imagem {
            width: 75%;
            height: 70%;
            max-width: 250px;
            max-height: 250px;
            img{
            width: 100%;
            height: 100%;
        }
        }
        .botao-add{
            width: 80%;
            height: 5rem;
            margin: 1rem;
        }
    }

</style>