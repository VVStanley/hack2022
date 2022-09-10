import {createStore} from 'vuex'

export default createStore({
  state: {
    authToken: localStorage.getItem('authToken') || null,
    username: localStorage.getItem('username') || null
  },
  getters: {
    isAuth: (state) => state.authToken,
    getUsername: (state) => state.username
  },
  mutations: {
    setUsername(state, username) {
      localStorage.setItem('username', username);
      state.username = username;
    },
    setAuthToken(state, token) {
      localStorage.setItem('authToken', token);
      state.auth = true;
    },
  },
  actions: {},
  modules: {}
})
