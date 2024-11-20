// src/stores/user.js
import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    token: localStorage.getItem('token') || null,
    user: null,
  }),

  actions: {
    async signup(payload) {
      try {
        const response = await axios.post('http://localhost:8000/accounts/signup/', payload);
        console.log('회원가입 성공:', response.data);
      } catch (error) {
        console.error('회원가입 오류:', error);
        throw error;
      }
    },

    async login(username, password) {
      try {
        if (!username || !password) {
          throw new Error('사용자 이름과 비밀번호는 필수 항목입니다.');
        }
    
        const response = await axios.post('http://localhost:8000/accounts/login/', {
          username,
          password,
        });
    
        this.token = response.data.token;
        localStorage.setItem('token', this.token);
        axios.defaults.headers.common['Authorization'] = `Token ${this.token}`;
        await this.fetchUser();
      } catch (error) {
        console.error('로그인 오류:', error);
        if (error.response && error.response.data) {
          console.error('서버 응답 오류 데이터:', error.response.data);
        }
        throw error;
      }
    },
    async fetchUser() {
      try {
        const response = await axios.get('http://localhost:8000/accounts/profile/');
        this.user = response.data;
      } catch (error) {
        console.error('사용자 정보 가져오기 오류:', error);
      }
    },
    async logout() {
      try {
        await axios.post('http://localhost:8000/accounts/logout/', null, {
          headers: { Authorization: `Token ${this.token}` },
        });
        this.token = null;
        this.user = null;
        localStorage.removeItem('token');
        delete axios.defaults.headers.common['Authorization'];
        console.log('로그아웃 성공');
      } catch (error) {
        console.error('로그아웃 오류:', error);
        throw error;
      }
    },
    async updateProfile(updatedInfo) {
  try {
    // username과 email 필드는 필수로, password는 선택적으로 포함
    const payload = {
      username: updatedInfo.username,
      email: updatedInfo.email,
    };

    // 비밀번호가 제공된 경우에만 payload에 추가
    if (updatedInfo.password) {
      payload.password = updatedInfo.password;
    }

    if (!payload.username || !payload.email) {
      throw new Error('모든 필수 필드를 입력해야 합니다.');
    }

    const response = await axios.put('http://localhost:8000/accounts/profile/', payload, {
      headers: {
        'Authorization': `Token ${this.token}`,
        'Content-Type': 'application/json'
      }
    });
    this.user = response.data;
    localStorage.setItem('user', JSON.stringify(this.user));
  } catch (error) {
    console.error('프로필 수정 오류:', error);
    if (error.response && error.response.data) {
      console.error('서버 응답 오류 데이터:', error.response.data);
    }
    throw error;
  }
}
  },
});
