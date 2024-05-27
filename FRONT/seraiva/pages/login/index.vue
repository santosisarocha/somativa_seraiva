<script setup lang="ts">
import FloatLabel from 'primevue/floatlabel';
import InputText from 'primevue/inputtext';
import Password from 'primevue/password';
import Button from 'primevue/button';
import { reactive, ref } from 'vue';

const{ signIn } = useAuth();

definePageMeta({
    layout: 'login'
})

    const credenciais = reactive({
        email: '',
        password: ''
    });
    const mensagemErro = ref('');

    const fazerLogin = ()=>{
        console.log("login: ", credenciais);
        signIn(credenciais, {redirect: false})
        .then(()=>{
            console.log("logado com sucesso .....");
            navigateTo('/')
        })
        .catch((error)=>{
            console.error("error: ", error)
            mensagemErro.value = 'Não foi possivel fazer o login com estas credenciais... ';
            setTimeout(()=>{
                mensagemErro.value = '';
                credenciais.email = '';
                credenciais.password = '';
            }, 3000);
        })
    } 


</script>

<template>
    <main class="login-main flex align-items-center justify-content-center">
        <section class="login-container flex flex-column align-items-center justify-content-center ">
            <img class="logo" src="public/logo.png" >
            <h4 class="row-login"> Seraiva </h4>
            <div class="row-login">
                <FloatLabel>
                    <InputText v-model="credenciais.email" type="email" id="email-input" class="input-text"/>
                    <label for="email-input">Email</label>
                </FloatLabel>
            </div>
            <div  class="row-login">
                <FloatLabel>
                    <InputText v-model="credenciais.password" type="password" id="password-input" class="input-text"/>
                    <label for="password-input">Senha</label>
                </FloatLabel>
                
            </div>
            <div class="row-login" v-if="mensagemErro !== ''">
                <p id="erro">{{ mensagemErro }}</p>
            </div>
            <div id="login-button">
                <Button @click="fazerLogin" label="Entrar" class="custom-button" ></Button>
            </div>

        </section>
    </main>
</template>

<style scoped lang="scss">
    .login-main{
        width: 100vw;
        height: 100vh;
        background-color: rgb(18, 15, 41);
        background-repeat: repeat;
        background-size: cover;


        .login-container{
            width: 30vw;
            height: 70vh;
            background-color: white;
            border-radius: 30px;

            .logo{
                width: 20vh;
                height: 20vh;

            }

            .row-login{
                margin: 1rem 0 1rem 0;
                .input-text{
                    height: 2.5rem;
                    width: 250px;
                }
                #login-button{
                    width: 100px;
                    height: 30px;
                
                }
                #erro{
                    color: tomato;
                    font-size: 0.8rem;
                }
            }
        }
        .custom-button {
        background-color: #50ab9e ;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    }

</style>