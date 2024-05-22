<script setup lang="ts">
import {getProdutos} from '~/services/produtos';
import { type Livro } from '~/models/produtos';
import { type Ref, ref } from 'vue';
import { onMounted } from 'vue';

const produtos: Ref<Array<Livro>> = ref([]);


const atualizarProdutos= () => {
    getProdutos().then((produtosEncontrados) => { 
        console.log("Produtos encontrados:", produtosEncontrados?.results[0].titulo);
        produtos.value = produtosEncontrados?.results ?? [];
});
};
atualizarProdutos();
</script>

<template>
    <main class="home-container flex flex-column align-items-center justify-content-center">
        <h1>Home</h1>
        <div class="produtos-container grid align-items-center justify-content-center">

            <div v-for="(produto,index) in produtos">
                <LivroItem :key="index" class="col-4" :produto="produto" />
            </div>
        

        </div>
    </main>
</template>

<style scoped lang="scss">
.home-container{
    margin: 0;
    width: 100vw;
    background-color: rgb(241, 243, 229);
    min-height: calc(100vh - var(--altura-header));
    // min-width: 50vh;
    
}

</style>