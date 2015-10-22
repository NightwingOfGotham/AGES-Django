/**
 * Factory: OfficerFactory
 */
angular.module('GalacticApp')
  .factory('OfficerFactory', function ShipFactory ($q, $http, $location) {
    'use strict';
    var exports = {};

    exports.officers = [];

    exports.goToShip = function(fleetId, shipId) {
      if ( angular.isNumber(fleetId) && angular.isNumber(shipId) ) {
        $location.path('command/fleet/' + fleetId + '/ship/' + shipId)
      }
    };

    exports.goToCommand = function() {
      $location.path('command/')
    };

    exports.goToFleet = function(fleetId) {
      if ( angular.isNumber(fleetId) ) {
        $location.path('command/fleet/' + fleetId)
      }
    };

    exports.goToCommand = function() {
      $location.path('command/')
    };

    exports.getOfficer = function (params) {
      if (params.officerId) {
        var deferred = $q.defer();
        return $http.get('/api/officer/' + params.officerId)
          .success(function (data) {
            exports.officers = [data];
            deferred.resolve(data);
          })
          .error(function (data) {
            deferred.reject(data);
          });
        return deferred.promise;
      }
    };

    return exports;
  });