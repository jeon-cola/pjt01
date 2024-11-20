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
        <li class="nav-item">
          <RouterLink :to="{name:'map'}"  id="link">map</RouterLink>
        </li>
        <li class="nav-item">
          <RouterLink :to="{name:'posts'}" id="link">게시물</RouterLink> <!-- 게시물 링크 추가 -->
        </li>
        <li class="nav-item" v-if="!isAuthenticated">
          <RouterLink :to="{name:'login'}" id="link">login</RouterLink>
        </li>
        <li class="nav-item" v-if="isAuthenticated">
          <button @click="handleLogout" id="link" style="background: none; border: none; cursor: pointer;">logout</button>
        </li>
        <li class="nav-item" v-if="isAuthenticated">
          <RouterLink :to="{name:'profile'}" id="link">나의 프로필</RouterLink>
        </li>
      </ul>
    </div>
  </div>

    </nav>


    <router-view/>
  
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { computed } from 'vue';
import { useUserStore} from '@/stores/user';
import 'bootstrap/dist/css/bootstrap.min.css';
// Bootstrap JS (옵션)
import 'bootstrap/dist/js/bootstrap.bundle.min.js';


const userStore = useUserStore();

// 로그인 상태 확인
const isAuthenticated = computed(() => userStore.token !== null);

// 로그아웃 처리 함수
const handleLogout = async () => {
  try {
    await userStore.logout({
      headers: { Authorization: `Token ${userStore.token}` }
    });
    alert('로그아웃 성공');
  } catch (error) {
    console.error('로그아웃 실패:')}
  }
</script>

<style  scoped>
#link {
  text-decoration: none;
  color: inherit;
  display: inline-block;  /* 또는 block */
  margin-right: 10px; 
}

</style>