/**
 * Factory: CommandFactory
 */
angular.module('GalacticApp')
  .factory('CommandFactory', function CommandFactory ($q, $http, $location) {
    'use strict';
    var exports = {};

    exports.fleets = [];

    exports.goToFleet = function(fleetId) {
      if ( angular.isNumber(fleetId) ) {
        $location.path('command/fleet/' + fleetId)
      }
    };

    exports.getFleets = function (params) {
      var deferred = $q.defer();
      return $http.get('/api/fleet/')
        .success(function (data) {
          exports.fleets = data.sort(compare);
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    function compare(a,b) {
      if (a.fleetId < b.fleetId)
        return -1;
      if (a.fleetId > b.fleetId)
        return 1;
      return 0;
    }

    return exports;
  });
