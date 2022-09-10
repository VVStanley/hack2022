<template>
  <h1>Login</h1>
  <hr>
  <form class="row g-3" v-on:submit.prevent="submitForm">
    <div class="col-auto">
      <label for="inputPassword2" class="visually-hidden">Password</label>
      <input type="text" v-model="user.username" class="form-control" placeholder="Логин ИННКПП">
      <input type="password" v-model="user.password" class="form-control" placeholder="Пароль">
    </div>
    <div class="col-auto">
      <button type="submit" class="btn btn-primary mb-3">Войти</button>
    </div>
  </form>
</template>

<script>
import axios from "@/axios/index";
import store from "@/store";

export default {
  name: "login",
  data() {
    return {
      user: {
        username: '273089390027301001',
        password: 11111,
      }
    }
  },
  mounted() {
    console.log(567567)
  },
  methods: {
    async submitForm() {
      console.log(this.user)
      await axios.post(
        '/auth/token/login',
          `grant_type=&username=${this.user.username}&password=${this.user.password}`,
          {
                headers: {"Content-Type": "application/x-www-form-urlencoded"}
            }

      ).then(
          ({data}) => {
            console.log(data)
            store.commit('setAuthToken', data.auth_token);
            store.commit('setUsername', this.user.username);
            console.log('us - ', store.getters.getUsername)
            window.location.reload();
          }
      ).catch(
          error => console.log(error.response.data)
      )
    }
  }
}
</script>

<style scoped>

</style>