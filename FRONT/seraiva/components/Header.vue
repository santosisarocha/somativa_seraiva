
import type { reduceEachLeadingCommentRange } from 'typescript';

import type { Header } from '#build/components';
<script setup lang="ts">
import {ref} from 'vue';

const itensMenu = ref([
    {
        label: 'Home',
        icon: 'pi pi-home'
    },
    {
        label: 'Carrinho',
        icon: 'pi pi-shopping-bag'
    },
    {
        label: 'Login',
        icon: 'pi pi-user'
    }
])

</script>

<template>
    <header>
        <div class="flex align-items-center justify-content-center">
            <Menubar :model="itensMenu" />
        </div>
    </header>
</template>

<style scoped lang="scss">
    header{
        width: 100vw;
        height: var(--altura-header);
        border-bottom: 1px;
        background-color: rgb(18, 15, 41);
        background-repeat: repeat;
        background-size: cover;;

        .p-menubar{
            height: 50px;
            border: none;
            background-color: rgb(18, 15, 41);
            color: white;

            .p-menuitem{
                margin: 0 1rem 0 1rem;
                color: white;
            }
            
        }

    }

</style>