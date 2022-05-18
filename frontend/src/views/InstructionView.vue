<template>
  <div style="margin-top: 1em !important">
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div class="card">
            <div class="card-body">
              <h6 class="card-title">Инструкция по работе с приложением</h6>
              <div id="content">
                <ul class="timeline">
                  <li class="event">
                      <h3>Установка</h3>
                      <p>Приложение можно скачать по ссылке или по QR коду.</p>
                      <p>Android: <a href="https://play.google.com/store/apps/details?id=com.TagProject" target="_blank">Google Play</a></p>
                      <img :src="qrcode_android" width="150px">
                  </li>
                  <li class="event">
                      <h3>Фото</h3>
                      <p>Фотографируйте место скопления произрастания амброзии. Желательно фотографировать именно куст амброзии в крупном виде.</p>
                  </li>
                  <li class="event">
                      <h3>Распознавание</h3>
                      <p>Сделанное фото распознается компьютерным зрением, то есть проходит машинную премодерацию.</p>
                  </li>
                  <li class="event">
                      <h3>Размещение на карте</h3>
                      <p>Распознанные фотографии с геометками отправляются на сервер, где размещаются на карте.</p>
                  </li>
                  <li class="event">
                      <h3>Администрация решит проблему</h3>
                      <p>Администрация г. Таганрога руководствуется полученной картой при планировании мероприятий по борьбе с сорной растительностью.</p>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'InstructionView',
  data: function () {
    return {
      qrcode_android: require('@/assets/images/qrcodes/android.png'),
    }
  },
}
</script>

<style scoped>
.card-title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 25px;
  line-height: 30px;
  text-align: center;
  margin-bottom: 1.5em;
}

.card {
  border: none;
}

body{margin-top:20px;}
.timeline {
    border-left: 3px solid #95E375;
    border-bottom-right-radius: 4px;
    border-top-right-radius: 4px;
    background: #82c96718;
    margin: 0 auto;
    letter-spacing: 0.2px;
    position: relative;
    line-height: 1.4em;
    font-size: 1.03em;
    padding: 50px;
    list-style: none;
    text-align: left;
    max-width: 40%;
}

@media (max-width: 767px) {
    .timeline {
        max-width: 98%;
        padding: 25px;
    }
}

.timeline h1 {
    font-weight: 300;
    font-size: 1.4em;
}

.timeline h2,
.timeline h3 {
    font-weight: 600;
    font-size: 1rem;
    margin-bottom: 10px;
}

.timeline .event {
    border-bottom: 1px dashed #e8ebf1;
    padding-bottom: 25px;
    margin-bottom: 25px;
    position: relative;
}

@media (max-width: 767px) {
    .timeline .event {
        padding-top: 30px;
    }
}

.timeline .event:last-of-type {
    padding-bottom: 0;
    margin-bottom: 0;
    border: none;
}

.timeline .event:before,
.timeline .event:after {
    position: absolute;
    display: block;
    top: 0;
}

.timeline .event:before {
    left: -207px;
    content: attr(data-date);
    text-align: right;
    font-weight: 100;
    font-size: 0.9em;
    min-width: 120px;
}

@media (max-width: 767px) {
    .timeline .event:before {
        left: 0px;
        text-align: left;
    }
}

.timeline .event:after {
    -webkit-box-shadow: 0 0 0 3px #95E375;
    box-shadow: 0 0 0 3px #95E375;
    left: -55.8px;
    background: #fff;
    border-radius: 50%;
    height: 9px;
    width: 9px;
    content: "";
    top: 5px;
}

@media (max-width: 767px) {
    .timeline .event:after {
        left: -31.8px;
    }
}

.rtl .timeline {
    border-left: 0;
    text-align: right;
    border-bottom-right-radius: 0;
    border-top-right-radius: 0;
    border-bottom-left-radius: 4px;
    border-top-left-radius: 4px;
    border-right: 3px solid #95E375;
}

.rtl .timeline .event::before {
    left: 0;
    right: -170px;
}

.rtl .timeline .event::after {
    left: 0;
    right: -55.8px;
}
</style>