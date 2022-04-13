# Task 4. (*) Попробуйте вручную (!) скопировать данные с сайта
# https://www.wunderground.com/history/daily/UKOO/date/2020-9-14
# https://www.wunderground.com/history/daily/UKOO/date/2022-1-1
# (там есть вкладка History и поищите на ней Daily Observations)
# и посчитать среднее давление за сутки, например.
# примечание: с начала войны много погодных сайтов отключилось - поэтому история не везде до последней даты.

with open('Daily_oservation.csv', 'r') as observat:
    pressure = []
    observat.readline()
    for line in observat.readlines():
        pressure.append(float(line.split(',')[8].replace('\xa0in', '')))
av_pressure = sum(pressure)/len(pressure)
print(f'The average pressure for all the day is:  {av_pressure:.3f}')
