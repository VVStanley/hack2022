<template>

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav" v-if="$store.getters.isAuth">
        <router-link class="nav-link" to="/supplier">Мои данные</router-link>
        <router-link class="nav-link" to="/contracts">Мои контракты</router-link>
        <router-link class="nav-link" to="/tru">Справочник товаров</router-link>
        <router-link class="nav-link" to="/mytru">Мои товары</router-link>
        <router-link class="nav-link" to="/consumers">Мои клиенты</router-link>

        <a href="http://172.20.26.3:8000/map/" target="_blank" class="nav-link">Карта поставщиков</a>

        <router-link class="nav-link " to="/logout">Выход</router-link>

      </div>
      <div class="navbar-nav" v-else>
        <router-link class="nav-link" to="/">Home</router-link>
        <router-link class="nav-link" to="/login">Login</router-link>
      </div>

    </div>
  </div>
</nav>
  <router-view/>
</template>

<script>

export default {
  name: 'App'
}
</script>
