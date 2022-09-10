<template>
<h1>Пока</h1>
</template>

<script>
export default {
  name: "Logout",
  mounted() {
    localStorage.removeItem('authToken');
    window.location.reload();
  }
}
</script>

<style scoped>

</style>