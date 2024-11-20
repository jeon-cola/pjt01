<template>
  <div>
    <h1>게시물 목록</h1>

    <!-- 게시물 작성 버튼 (로그인된 사용자만 작성 가능) -->
    <button v-if="isAuthenticated" @click="openCreatePostModal">게시물 작성</button>
    <p v-else>로그인해야 게시물을 작성할 수 있습니다.</p>

    <div v-for="post in posts" :key="post.id" class="post">
      <h2>{{ post.title }}</h2>
      <p>{{ post.content }}</p>
      
      <!-- 게시물 삭제 버튼 (작성자만 삭제 가능) -->
      <button v-if="isAuthenticated" @click="deletePost(post.id)">게시물 삭제</button>

      <!-- 댓글 목록 -->
      <div class="comments" v-if="post.comments.length > 0">
        <h4>댓글</h4>
        <div v-for="comment in post.comments" :key="comment.id" class="comment">
          <p>{{ comment.text }}</p>
        </div>
      </div>

      <!-- 댓글 작성 폼 (로그인된 사용자만 작성 가능) -->
      <div v-if="isAuthenticated" class="comment-form">
        <input v-model="newComment" placeholder="댓글 작성" />
        <button @click="addComment(post.id)">댓글 달기</button>
      </div>
      <p v-else>로그인해야 댓글을 작성할 수 있습니다.</p>
    </div>

    <!-- 게시물 작성 모달 -->
    <CreatePostModal
      v-if="isCreatePostModalOpen"
      @close="closeCreatePostModal"
      @post-created="addPost"
    />
  </div>
</template>

<script>
import { computed, ref, onMounted } from 'vue';
import { useUserStore } from '@/stores/user';
import CreatePostModal from '@/components/CreatePostModal.vue'; // 게시물 작성 모달 컴포넌트

export default {
  components: { CreatePostModal },
  setup() {
    const userStore = useUserStore();

    // 로그인 상태 확인
    const isAuthenticated = computed(() => userStore.token !== null);
    const user = computed(() => userStore.user);

    // 게시물 및 댓글 관련 데이터 및 메서드
    const posts = ref([]);

    const newComment = ref('');
    const isCreatePostModalOpen = ref(false);

    // 게시물 데이터 로드하기 (예를 들어 localStorage를 통해)
    const loadPosts = () => {
      const storedPosts = localStorage.getItem('posts');
      if (storedPosts) {
        posts.value = JSON.parse(storedPosts);
      }
    };

    // 게시물 데이터 저장하기 (예를 들어 localStorage를 통해)
    const savePosts = () => {
      localStorage.setItem('posts', JSON.stringify(posts.value));
    };

    // 게시물 작성 모달 열기
    const openCreatePostModal = () => {
      isCreatePostModalOpen.value = true;
    };

    // 게시물 작성 모달 닫기
    const closeCreatePostModal = () => {
      isCreatePostModalOpen.value = false;
    };

    // 새로운 게시물 추가하기
    const addPost = (newPost) => {
      posts.value.push({
        id: posts.value.length + 1,
        title: newPost.title,
        content: newPost.content,
        comments: [],
      });
      savePosts(); // 변경 사항 저장
    };

    // 게시물 삭제하기
    const deletePost = (postId) => {
      posts.value = posts.value.filter((post) => post.id !== postId);
      savePosts(); // 변경 사항 저장
    };

    // 댓글 추가하기 (로그인한 경우에만 호출 가능)
    const addComment = (postId) => {
      if (newComment.value.trim() === '') return;

      const post = posts.value.find((p) => p.id === postId);
      if (post) {
        post.comments.push({
          id: post.comments.length + 1,
          text: newComment.value,
        });
        newComment.value = '';
        savePosts(); // 변경 사항 저장
      }
    };

    onMounted(() => {
      loadPosts(); // 컴포넌트가 마운트될 때 게시물 데이터를 로드합니다.
    });

    return {
      isAuthenticated,
      user,
      posts,
      newComment,
      isCreatePostModalOpen,
      openCreatePostModal,
      closeCreatePostModal,
      addPost,
      deletePost,
      addComment,
    };
  },
};
</script>

<style scoped>
/* 스타일 작성 */
.post {
  border: 1px solid #ccc;
  padding: 1rem;
  margin-bottom: 1rem;
}
.comment-form {
  margin-top: 1rem;
}
</style>
