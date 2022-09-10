<template>
<nav>
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#">Первая</a></li>
    <li class="page-item"><a class="page-link" :href="previous">Назад</a></li>
    <li class="page-item"><a class="page-link" :href="next">Вперед</a></li>
    <li class="page-item"><a class="page-link" href="#">Последняя</a></li>
  </ul>
</nav>
</template>

<script>
export default {
  name: "paginator",
  props: {
    next: String,
    previous: String,
  },
  mounted() {
    console.log( '--', this.next)
    console.log( '--', this.previous)
  }
}
</script>

<style scoped>

</style>