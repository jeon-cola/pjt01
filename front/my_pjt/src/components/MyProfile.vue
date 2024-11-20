<template>
  <div class="profile">
    <h1>나의 프로필</h1>
    <div v-if="user">
      <p><strong>사용자 이름:</strong> {{ user.username }}</p>
      <p><strong>이메일:</strong> {{ user.email }}</p>
      <button @click="goToEditProfile">정보 수정</button>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const userStore = useUserStore();
    const user = computed(() => userStore.user);
    const router = useRouter();

    const goToEditProfile = () => {
      router.push({ name: 'editProfile' }); // 수정 페이지로 라우팅
    };

    return {
      user,
      goToEditProfile,
    };
  },
};
</script>

<style scoped>
.profile {
  padding: 2rem;
}
</style>
