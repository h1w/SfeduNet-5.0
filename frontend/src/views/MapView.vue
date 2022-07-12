<template>
  <div>
    <div id="map-container">
      <SimpleMap />
    </div>

    <div id="hidden-about-project-icon" v-if="aboutButtonHidden == false">
      <b-card id="hidden-about-project-icon-card" no-body class="overflow-hidden text-center" style="max-width: 10em;">
        <b-row no-gutters>
          <b-col>
            <b-button @click="aboutButtonHidden = !aboutButtonHidden" id="about-show-button"><img id="hidden-about-project-icon-card-button-logo" :src="aboutProjectCardLogoSVG"><img id="hidden-about-project-icon-card-button-logo-2" :src="aboutProjectHideLogoSVG"></b-button>
          </b-col>
        </b-row>
      </b-card>
    </div>

    <div id="about-project" v-if="aboutButtonHidden == true">
      <b-card id="about-card" no-body class="overflow-hidden text-center" style="max-width: 20em;">
        <b-row no-gutters>
          <b-col>
            <b-card-body class="text-center" title="О проекте">
              <b-card-text>
                Любой желающий может скачать приложение и фотографировать кусты амброзии, создавая метки ее произрастания на карте.
              </b-card-text>
              
              <b-card-text>
                Это поможет администрации города бороться с сорной растительностью.
              </b-card-text>
            </b-card-body>

            <b-button :to="{name: 'instruction'}" id="about-button"><img id="about-card-button-logo" :src="aboutProjectCardLogoSVG">К приложению</b-button>
            <br>
            <b-button @click="aboutButtonHidden = !aboutButtonHidden" id="about-hide-button">скрыть <img id="about-card-hide-button-logo" :src="aboutProjectHideLogoSVG"></b-button>
          </b-col>
        </b-row>
      </b-card>
    </div>
    
    <!-- <div id="footer-right" class="float-right">
      <p>Сделано в <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="#F53838" viewBox="0 0 16 16" class="bi bi-suit-heart-fill"><path d="M4 1c2.21 0 4 1.755 4 3.92C8 2.755 9.79 1 12 1s4 1.755 4 3.92c0 3.263-3.234 4.414-7.608 9.608a.513.513 0 0 1-.784 0C3.234 9.334 0 8.183 0 4.92 0 2.755 1.79 1 4 1z"></path></svg><a href="https://vk.com/sfedunet" target="_blank" class="text-900" style="text-decoration: none; color: rgb(122, 131, 158) !important;">SfeduNET</a></p>
    </div> -->
  </div>
</template>

<script>
import SimpleMap from '@/components/Map/SimpleMap.vue'

export default {
  name: 'MapView',
  mounted() {
    document.title = 'Карта | Амброзия'
  },
  data: function () {
    return {
      aboutProjectCardLogoSVG: require('@/assets/About_Project_Card_Logo.svg'),
      aboutProjectHideLogoSVG: require('@/assets/About_Project_Hide_Card_Logo.svg'),
      aboutButtonHidden: false,
    }
  },
  components: {
    SimpleMap,
  },
}
</script>

<style scoped>
#footer-right {
  position: absolute;
  right: 0;
  bottom: 0;
  z-index: 9999999999;
  margin-right: 0.5em;
}



#map-container {
  position: absolute;
  height: auto;
  width: 100%;
  top: 4.2em;
  bottom: 0;
  right: 0;
  left: 0;
}

#map-container > div {
  width: 100%;
  height: 100%;
}

#about-project {
  position: absolute;
  z-index: 999999;
  right: 0;
  top: 35%;
  margin-right: 1em !important;
}

#about-card {
  background-color: #FFFFFF;
  border-radius: 25px;
}

#about-button {
  /* margin-bottom: 2em; */
  background-color: #95E375;
  border-color: #95E375;
  border-radius: 26.1817px;
  
  color: #000000;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-size: 15px;
  line-height: 22px;
  width: 80%;
}

#about-card-button-logo {
  width: 1.3em;
  height: auto;
  margin-right: 0.3em;
}

.card-title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 22px;
  line-height: 30px;
  text-align: center;

  color: #000000;

  margin-top: 0.4em;
  margin-bottom: 1em;
}

.card-text {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 16px;
  line-height: 22px;
  text-align: center;

  color: #000000;
}

#about-hide-button {
  margin-bottom: 1em;
  margin-top: 1.8em;
  background-color: #ffffff00;
  border-color: #ffffff00;
  border-radius: 26.1817px;
  height: 2em;
  width: 40%;

  color: #000000;
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-size: 13px;
  line-height: 15px;

  outline: none !important;
  box-shadow: none !important;
}

#about-card-hide-button-logo {
  width: 0.5em;
  height: auto;
  color: #000000;
  margin-left: 0.4em;
}

#hidden-about-project-icon {
  position: absolute;
  z-index: 999999;
  right: 0;
  top: 35%;
  margin-right: 1em !important;
}

#hidden-about-project-icon-card {
  background-color: #FFFFFF;
  box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  border-radius: 37.0968px;
}

#about-show-button {
  background-color: #00000000;
  border-color: #00000000;
  border-radius: 26.1817px;
  
  color: #000000;

  margin-top: 0.4em;
  margin-bottom: 0.4em;
  margin-left: 0.7em;
  margin-right: 0.7em;
}

#hidden-about-project-icon-card-button-logo {
  width: 2em;
  height: auto;
  background-color: #95E375;
  border-color: #95E375;
  border-radius: 50%;
  padding: 0.2em;
}

#hidden-about-project-icon-card-button-logo-2 {
  width: 1.0em;
  height: auto;
  margin-left: 0.6em;
  transform: rotate(180deg);
}

#about-show-button.btn:focus {
  outline: none !important;
  box-shadow: none !important;
}

</style>