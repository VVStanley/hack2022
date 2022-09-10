<template>
<h1>Пока</h1>
</template>

<script>
export default {
  name: "Logout",
  mounted() {
    localStorage.setItem('authToken', '');
    window.location.reload();
  }
}
</script>

<style scoped>

</style>