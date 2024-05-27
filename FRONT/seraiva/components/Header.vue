
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
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-home mr-1"></i>
          <NuxtLink to="/">Home</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-briefcase mr-1"></i>
          <NuxtLink to="/login">Login</NuxtLink>
        </div>
        <div class="menu-item flex align-items-center justify-content-center mr-4">
          <i class="pi pi-shopping-cart mr-1"></i>
          <NuxtLink to="/emprestimo">Carrinho</NuxtLink>
        </div>
    </header>
</template>

<style scoped lang="scss">
header {
  width: 100vw;
  height: var(--altura-header);
  display: flex;
  justify-content: space-around;
  align-items: center;

  .menu-item{
    height: var(--altura-header);
    display: flex;
    align-items: center;
    
    a{
      text-decoration: none;
      color: black;
    }
    &:hover{
      transform: scale(1.1);
    }
  }
}

</style>