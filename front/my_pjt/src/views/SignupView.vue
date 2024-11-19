<template>
  <div>
    <h1>sign up</h1>
    <RouterLink :to="{name:'login'}">login</RouterLink>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink,RouterView } from 'vue-router';
</script>

<style  scoped>

</style>