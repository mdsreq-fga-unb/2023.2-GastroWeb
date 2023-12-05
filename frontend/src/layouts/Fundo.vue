<template>
  <q-layout :view="'hHh Lpr lff'" class="full-width" style="display: flex; justify-content: center; align-items: center;">
    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: 'FundoLogin',
  components: {},
  data() {
    return {}
  }
}
</script>