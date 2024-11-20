<template>
  <div>
    <h2>회원가입</h2>
    <form @submit.prevent="handleSignup">
      <input v-model="username" placeholder="사용자 이름" required />
      <input v-model="email" type="email" placeholder="이메일" required />
      <input v-model="password" type="password" placeholder="비밀번호" required />
      <input v-model="subscribedProducts" placeholder="가입한 상품 (쉼표로 구분)" />
      <button type="submit">가입하기</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useUserStore } from '@/stores/user';
import { useRouter } from 'vue-router';

export default {
  setup() {
    const userStore = useUserStore();
    const router = useRouter();

    const username = ref('');
    const email = ref('');
    const password = ref('');
    const subscribedProducts = ref('');

    const handleSignup = async () => {
      try {
        const payload = {
          username: username.value,
          email: email.value,
          password: password.value,
          subscribed_products: subscribedProducts.value,
        };
        await userStore.signup(payload);
        alert('회원가입 성공');
        router.push('/login');
      } catch (error) {
        console.error('회원가입 실패:', error);
        if (error.response && error.response.data) {
          alert(`회원가입 실패: ${JSON.stringify(error.response.data)}`);
        } else {
          alert('회원가입 실패');
        }
      }
    };

    return {
      username,
      email,
      password,
      subscribedProducts,
      handleSignup,
    };
  },
};
</script>
