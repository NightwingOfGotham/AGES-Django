/**
 * Factory: ShipFactory
 */
angular.module('GalacticApp')
  .factory('ShipFactory', function ShipFactory ($q, $http, $location) {
    'use strict';
    var exports = {};

    exports.officers = [];

    exports.goToOfficer = function(fleetId, shipId, officerId) {
      if ( angular.isNumber(fleetId) && angular.isNumber(shipId) && angular.isNumber(officerId) ) {
        $location.path('command/fleet/' + fleetId + '/ship/' + shipId + '/officer/' + officerId)
      }
    };

    exports.goToFleet = function(fleetId) {
      if ( angular.isNumber(fleetId) ) {
        $location.path('command/fleet/' + fleetId)
      }
    };

    exports.goToCommand = function() {
      $location.path('command/')
    };

    exports.getOfficers = function (shipId) {
      var deferred = $q.defer();
      return $http.get('/api/officer/')
        .success(function (data) {
          exports.officers = getShipOfficers(data, shipId);
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    function getShipOfficers (data, shipId) {
      var officers = [];
      for (var index in data) {
        var ship = data[index];
        if (ship.id == shipId) {
          officers.push(data[index]);
        }
      }
      return officers;
    }

    return exports;
  });