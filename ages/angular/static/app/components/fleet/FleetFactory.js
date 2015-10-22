/**
 * Factory: FleetFactory
 */
angular.module('GalacticApp')
  .factory('FleetFactory', function FleetFactory ($q, $http, $location) {
    'use strict';
    var exports = {};

    exports.ships = [];

    exports.goToShip = function(fleetId, shipId) {
      if ( angular.isNumber(shipId) && angular.isNumber(fleetId) ) {
        $location.path('command/fleet/' + fleetId + '/ship/' + shipId);
      }
    };

    exports.goToCommand = function() {
      $location.path('command/');
    };

    exports.getShips = function (fleetId) {
      var deferred = $q.defer();
      return $http.get('/api/ship/')
        .success(function (data) {
          exports.ships = getFleetShips(data, fleetId);
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    function getFleetShips (data, fleetId) {
      var ships = [];
      for (var index in data) {
        var ship = data[index];
        if (ship.fleet == fleetId) {
          ships.push(data[index]);
        }
      }
      return ships;
    }

    return exports;
  });