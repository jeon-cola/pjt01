<template>
  <div>
    <h2 v-if="!isAuthenticated">로그인</h2>
    <form v-if="!isAuthenticated" @submit.prevent="handleLogin">
      <input v-model="username" placeholder="사용자 이름" required />
      <input v-model="password" type="password" placeholder="비밀번호" required />
      <button type="submit">로그인</button>
    </form>

    <div v-if="!isAuthenticated">
      <h5>아이디가 없으십니까?</h5>
      <div>회원가입 하기</div>
      <RouterLink :to="{ name: 'signup' }">회원가입</RouterLink>
    </div>

    <!-- 로그아웃 버튼 추가 -->
    <div v-if="isAuthenticated">
      <h2>프로필</h2>
      <p>{{ userProfile.username }}님 환영합니다!</p>
      <button @click="handleLogout">로그아웃</button>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const userStore = useUserStore();
    const router = useRouter();

    const username = ref('');
    const password = ref('');

    // 로그인 상태 확인을 위한 computed property
    const isAuthenticated = computed(() => userStore.isAuthenticated);
    const userProfile = computed(() => userStore.user);

    // 로그인 처리 함수
    const handleLogin = async () => {
      try {
        await userStore.login(username.value, password.value);
        alert('로그인 성공');
        router.push('/profile'); // 로그인 성공 후 프로필 페이지로 이동
      } catch (error) {
        console.error('로그인 실패:', error);
        alert('로그인 실패: ' + (error.response?.data?.detail || error.message));
      }
    };

    // 로그아웃 처리 함수
    const handleLogout = async () => {
      try {
        await userStore.logout();
        alert('로그아웃 성공');
        router.push('/'); // 로그아웃 후 홈 페이지로 이동
      } catch (error) {
        console.error('로그아웃 실패:', error);
        alert('로그아웃 실패: ' + (error.response?.data?.detail || error.message));
      }
    };

    return {
      username,
      password,
      handleLogin,
      handleLogout,
      isAuthenticated,
      userProfile,
    };
  },
};
</script>
