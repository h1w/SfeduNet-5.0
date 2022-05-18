<template>
  <div style="margin-top: 1em !important;">
    <b-container >
      <h6 id="page-title">Волонтерство</h6>
      <div class="row justify-content-center">
        <div class="col-xs-12 col-sm-6 col-lg-8">
          <b-card class="text-center" img-src="https://i.imgur.com/Qlda5MN.png" img-alt="Card image" img-top>
            <b-card-text>
              Простыми действиями мы с вами можем внести существенный вклад в благоустройство городской среды.
            </b-card-text>
            
            <b-card-text>
              Просто скачайте приложение по инструкции выше и фотографируйте проблемные участки с амброзией.
            </b-card-text>

            <b-card-text>
              После прохождения премодерации фотографии размещаются на карте.
            </b-card-text>

            <b-card-text>
              Далее с полученные данные берёт в работу Администрация города.
            </b-card-text>

            <b-card-text>
              Давайте вместе сделаем Таганрог комфортнее для людей!
            </b-card-text>
          </b-card>
        </div>
      </div>
    </b-container>
  </div>
</template>

<script>
export default {
  name: 'VolunteeringView',
  data: function () {
    return {

    }
  },
}
</script>

<style scoped>
.card-img-top {
  padding: 1em;
  border-radius: 21px;
}

.card {
  border: none;
}

#page-title {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-size: 25px;
  line-height: 30px;
  text-align: center;
  margin-bottom: 1.5em;
}

b-card-text {
  font-family: 'Inter';
  font-style: normal;
}
</style>