<template>
    <div class="homeContent">
        <div class="block">
            <div class="group"><img class="item" src="../assets/ukey.png" alt=""><p class="title">Ukey管理</p></div>
            <div class="group"><img class="item" src="../assets/company.png" alt=""><p class="title">单位管理</p></div>
            <div class="group"><img class="item" src="../assets/companyManage.png" alt=""><p class="title">管口股室维护</p></div>
        </div>
    </div>
</template>
<script>
export default {
  data () {
    return {
    }
  },
  methods: {
    seeting () {
      this.$router.push('/seeting')
    }
  },
  created () {
  }
}
</script>
<style lang= "less" scoped>
.homeContent{
    width: 100%;
    height: 100%;
    position: fixed;
    background-image: url('../assets/backgroundImg2.jpg');
    background-repeat:no-repeat;
    background-size:cover;
    display: flex;
    align-items: center;
    justify-content: center;
}
.block{
    display: flex;
    justify-content: center;
    align-content: center;
    width: 855px;
    flex-wrap: wrap;
}
.group{
    width: 170px;
    height: 170px;
}
.item{
    width: 119px;
    height: 119px;
    border-radius: 50%;
    margin: 25px 25px 0 25px;
    cursor: pointer;
}
.item:hover{
    width: 120px;
    height: 120px;
    border-radius: 50%;
    margin: 25px 25px 0 25px;
    border: 1px solid #eee;
    box-shadow: 0 0 20px #ddd;
}
.title{
    text-align: center;
    margin: 0px;
}
</style>
