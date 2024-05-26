<script setup lang="ts">
import {getProdutos} from '~/services/produtos';
import { type Livro } from '~/models/produtos';
import { type Ref, ref } from 'vue';
import { onMounted } from 'vue';


const livros: Ref<Array<Livro>> = ref([]);


const atualizarProdutos= () => {
    getProdutos().then((produtosEncontrados) => { 
        console.log("Produtos encontrados:", produtosEncontrados?.results);
        livros.value = produtosEncontrados?.results ?? [];
});
};
atualizarProdutos();

const painel = ref();

const toggle = (event: any) => {
    painel.value.toggle(event);
}
</script>

<template>
    <main class="home-container flex flex-column align-items-center justify-content-center">
        <h1>Home</h1>

        <div class="chatbot">
            <Button type="button" icon="pi pi-comment" label="Chatbot" @click="toggle" />
            <OverlayPanel ref="painel">
                <iframe width="350" height="430" allow="microphone;" src="https://console.dialogflow.com/api-client/demo/embedded/cbf3d547-68ab-4213-9a8c-96cd5336d530"></iframe>
            </OverlayPanel>
        </div>

        <div class="produtos-container grid align-items-center justify-content-center">

            <div v-for="(livro,index) in livros" :key="index">
                <ProdutoItem :key="index" class="col-4" :livro="livro" />
                
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
.chatbot{
    position: fixed;
    top: 0;
    right: 0;
    margin: 1rem
}

</style>