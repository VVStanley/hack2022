<template>

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav" v-if="$store.getters.isAuth">
        <router-link class="nav-link" to="/supplier">Поставщик</router-link>
        <router-link class="nav-link" to="/tru">TRU</router-link>
        <router-link class="nav-link" to="/logout">Logout</router-link>

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
