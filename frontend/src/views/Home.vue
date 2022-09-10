<template>
<h1>123</h1>
</template>

<script>

import store from "@/store";

export default {
  name: "Home",
  mounted() {
    console.log('us - ', store.getters.getUsername)
  }
};
</script>