<template>
    <div>
        <h1>vue 组件root</h1>
        <span>{{msg}}</span>
    </div>
</template>
<script>
export default {
    data() {
        return {
            msg:'app组件中的数据',
        }
    },
}
</script>
<style scoped>
    h1{
        width: 500px;
        background-color: aqua
    }
</style>