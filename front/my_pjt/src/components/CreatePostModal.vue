<template>
  <div class="modal-backdrop" @click.self="closeModal">
    <div class="modal-content">
      <h2>게시물 작성</h2>
      <input v-model="title" placeholder="제목" />
      <textarea v-model="content" placeholder="내용"></textarea>
      <div class="actions">
        <button @click="createPost">게시물 작성</button>
        <button @click="closeModal">취소</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, defineEmits } from 'vue';

const emit = defineEmits(['close', 'post-created']); // close와 post-created 이벤트 정의

// 데이터 선언
const title = ref('');
const content = ref('');

// 게시물 작성 함수
const createPost = () => {
  if (title.value.trim() && content.value.trim()) {
    // 작성한 게시물 데이터를 부모 컴포넌트에 전달
    emit('post-created', { title: title.value, content: content.value });

    // 작성 후 모달 닫기
    emit('close');
  } else {
    alert('제목과 내용을 입력하세요.');
  }
};

// 모달 닫기 함수
const closeModal = () => {
  emit('close'); // 모달 닫기 이벤트 방출
};
</script>

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: white;
  padding: 2rem;
  border-radius: 8px;
  width: 400px;
}

.actions {
  margin-top: 1rem;
  display: flex;
  justify-content: space-between;
}
</style>
