def convertToDays(period_type, timeToElapse):
  if period_type == 'days':
    return timeToElapse

  elif period_type == 'weeks':
    return timeToElapse * 7

  elif period_type == 'months':
    return timeToElapse * 30

  else:
    return 'Incorrect input'



# data = {
# 'region': {
#     'name': "Africa",
#     'avgAge': 19.7,
#     'avgDailyIncomeInUSD': 5,
#     'avgDailyIncomePopulation': 0.71
#     },
#   'periodType': "days",
#   'timeToElapse': 58,
#   'reportedCases': 674,
#   'population': 66622705,
#   'totalHospitalBeds': 1380614
# }

def estimator(data):
  
  data['timeToElapse'] = convertToDays(data['periodType'], data['timeToElapse'])

  outputData = {
    'data': data,
    'impact' : {
      'currentlyInfected' : data['reportedCases'] * 10,
    },

    'severeImpact' : {
      'currentlyInfected' : data['reportedCases'] * 50,
    }

  }


  days = 2 ** int((data['timeToElapse']/3))
  beds = int(outputData['data']['totalHospitalBeds'] * 0.35)
  outputData['impact']['infectionsByRequestedTime'] = outputData['impact']['currentlyInfected'] * days
  outputData['severeImpact']['infectionsByRequestedTime'] = outputData['severeImpact']['currentlyInfected'] * days
  outputData['impact']['severeCasesByRequestedTime'] = outputData['impact']['infectionsByRequestedTime'] * 0.15
  outputData['severeImpact']['severeCasesByRequestedTime'] = outputData['severeImpact']['infectionsByRequestedTime'] * 0.15
  outputData['impact']['hospitalBedsByRequestedTime'] =  beds - outputData['impact']['severeCasesByRequestedTime']
  outputData['severeImpact']['hospitalBedsByRequestedTime'] = beds - outputData['severeImpact']['severeCasesByRequestedTime']
  outputData['impact']['casesForICUByRequestedTime'] = int((outputData['impact']['infectionsByRequestedTime'] * (5/100), 2))
  outputData['severeImpact']['casesForICUByRequestedTime'] = int((outputData['severeImpact']['infectionsByRequestedTime'] * (5/100), 2))
  outputData['impact']['casesForVentilatorsByRequestedTime'] = int((outputData['impact']['infectionsByRequestedTime'] * (2/100), 2))
  outputData['severeImpact']['casesForVentilatorsByRequestedTime'] = int((outputData['severeImpact']['infectionsByRequestedTime'] * (2/100), 2))
  outputData['impact']['dollarsInFlight'] = int((outputData['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / data['timeToElapse'])
  outputData['severeImpact']['dollarsInFlight'] = int((outputData['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD']) / data['timeToElapse'])
    

  return outputData