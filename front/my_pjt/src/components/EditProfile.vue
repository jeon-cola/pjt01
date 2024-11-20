<template>
  <div class="profile-edit">
    <h1>프로필 수정</h1>
    <div v-if="editableUser">
      <p><strong>사용자 이름:</strong> <input v-model="editableUser.username" /></p>
      <p><strong>이메일:</strong> <input v-model="editableUser.email" /></p>
      <p><strong>비밀번호 (필수):</strong> <input v-model="password" type="password" placeholder="비밀번호를 입력해주세요" /></p>
      <button @click="updateProfile">저장</button>
    </div>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import { computed, ref } from 'vue';
import { useUserStore } from '@/stores/user';

export default {
  setup() {
    const userStore = useUserStore();
    const user = computed(() => userStore.user);
    const editableUser = ref({ ...user.value });
    const password = ref(''); // 비밀번호 필드 추가
    const errorMessage = ref(''); // 에러 메시지 저장

    const updateProfile = async () => {
      // 필수 입력 필드 확인
      if (!editableUser.value.username.trim() || !editableUser.value.email.trim() || !password.value.trim()) {
        alert('사용자 이름, 이메일, 비밀번호를 모두 입력해주세요.');
        return;
      }

      // 기존 이메일과 동일하다면 서버 요청 생략
      if (editableUser.value.email === user.value.email) {
        alert('이메일이 기존과 동일합니다. 변경된 내용이 없습니다.');
        return;
      }

      try {
        // 프로필 업데이트 요청
        await userStore.updateProfile({
          username: editableUser.value.username,
          email: editableUser.value.email,
          password: password.value,
        });
        alert('프로필이 수정되었습니다.');
      } catch (error) {
        console.error('프로필 수정 오류:', error);
        if (error.response && error.response.data) {
          console.error('서버 응답 오류 데이터:', error.response.data);
          
          // 서버로부터 받은 오류 메시지를 사용자에게 표시
          if (error.response.data.email) {
            errorMessage.value = `이메일 오류: ${error.response.data.email[0]}`;
          } else if (error.response.data.password) {
            errorMessage.value = `비밀번호 오류: ${error.response.data.password[0]}`;
          } else {
            errorMessage.value = '알 수 없는 오류가 발생했습니다.';
          }
        } else {
          errorMessage.value = '프로필 수정에 실패했습니다.';
        }
      }
    };

    return {
      editableUser,
      password,
      updateProfile,
      errorMessage,
    };
  },
};
</script>

<style scoped>
.profile-edit {
  padding: 2rem;
}

.error {
  color: red;
  margin-top: 1rem;
}
</style>
