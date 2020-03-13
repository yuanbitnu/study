<template>
    <div class="user">
        <h1>user id is {{id}} name is {{name}} age is {{age}}</h1>
    </div>
</template>

<script>
export default {
  name: 'tab_one',
  props: ['id', 'name', 'age']
}
</script>
