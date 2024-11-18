<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary" style="background-color: transparent;  opacity: 1;">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <RouterLink :to="{name:'home'}" id="link">home</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name:'saving'}"  id="link">saving</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name:'deposit'}"  id="link">deposit</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name:'exchange_rate'}"  id="link">exchange_rate</RouterLink>
        </li>
      </ul>
    </div>
  </div>

    </nav>


    <router-view/>
  
  </div>
</template>

<script setup>
import { RouterLink,RouterView } from 'vue-router';
import 'bootstrap/dist/css/bootstrap.min.css';
// Bootstrap JS (옵션)
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
</script>

<style  scoped>
#link {
  text-decoration: none;
  color: inherit;
  display: inline-block;  /* 또는 block */
  margin-right: 10px; 
}

</style>