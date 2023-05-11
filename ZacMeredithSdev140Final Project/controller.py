# This python file imports the view and weather
from view import View
from Weather import Weather


class Controller:

    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()

        self.updateGUI()

    def main(self):
        self.view.main()

    # this portion lets the GUI give an error whenever you enter a misspelled city
    def updateGUI(self):
        if 'error' not in self.weather.weatherData:
            self.view.varLocation.set(self.weather.getLocation())
            self.view.varCondition.set(self.weather.getConditionText())
            self.view.varWindSpeed.set(self.weather.getWindSpeedMPH())
            self.view.varWindDir.set(self.weather.getWindDirection())

            if self.view.varUnits.get() == 1:
                self.view.varTemp.set(self.weather.getCurrentTempF())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeF())
            else:
                self.view.varTemp.set(self.weather.getCurrentTempC())
                self.view.varFeelsLike.set(self.weather.getFeelsLikeC())

    def handleButtonSearch(self, ):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.updateGUI()

    def handleComboLocation(self):
        pass
