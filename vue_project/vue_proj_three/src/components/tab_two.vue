<template>
    <div class="tab_one">
        <h1>tab_two tab is {{id}} name is {{name}} gander is {{gander}}</h1>
    </div>
</template>

<script>
export default {
  name: 'tab_two',
  props: ['id', 'name', 'gander']
}
</script>
