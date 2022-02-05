<template>
  <div class="toggle" id="toggle" :click="expand">
    <i class="fa fa-plus" id="plus"></i>
  </div>
  <div class="menu" id="menu">
    <a href="#">
      <i class="fa fa-microphone"></i>
    </a>
    <a href="#">
      <i class="fa fa-user"></i>
    </a>
    <a href="#">
      <i class="fa fa-video-camera"></i>
    </a>
    <a href="#">
      <i class="fa fa-envelope"></i>
    </a>
    <a href="#">
      <i class="fa fa-camera"></i>
    </a>
    <a href="#">
      <i class="fa fa-bell"></i>
    </a>
  </div>
</template>
<script>
import { defineComponent } from "vue";

export default defineComponent({
    methods: {
        expand() {
            var i = 0;
            if (i == 0) {
                document.getElementById("menu").style.transform = "scale(3)";
                document.getElementById("plus").style.transform = "rotate(45deg)";
                i = 1;
            } else {
                document.getElementById("menu").style.transform = "scale(0)";
                document.getElementById("plus").style.transform = "rotate(0deg)";
                i = 0;
            }
        }
    }
});

</script>
<style scoped>
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css');

.toggle {
  background-color: #c87f8a;
  text-align: center;
  height: 100px;
  width: 100px;
  border-radius: 50%;
  position: absolute;
  margin: auto;
  top: 0px;
  bottom: 0px;
  left: 0px;
  right: 0px;
}

.fa-plus {
  font-size: 60px;
  color: white;
  display: block;
  margin-top: 20px;
  transition: 0.2s;
}

.menu {
  background-color: white;
  height: 100px;
  width: 100px;
  transform: scale(0);
  border-radius: 50%;
  border-style: double;
  border-color: #c87f8a;
  position: absolute;
  margin: auto;
  top: 0px;
  bottom: 0px;
  left: 0px;
  right: 0px;
  z-index: -1;
  transition: 0.2s;
}

a {
  display: inline-block;
  position: absolute;
  font-size: 15px;
  color: #bbbbbb;
}

a:nth-child(1) {
  top: 6px;
  left: 45px;
}

a:nth-child(2) {
  top: 24px;
  left: 77px;
}

a:nth-child(3) {
  top: 58px;
  left: 76px;
}

a:nth-child(4) {
  top: 78px;
  left: 42px;
}

a:nth-child(5) {
  top: 58px;
  left: 10px;
}

a:nth-child(6) {
  top: 23px;
  left: 12px;
}

a:hover {
  color: #c87f8a;
}
</style>
