/**
 * Factory: CommandFactory
 */
angular.module('GalacticApp')
  .factory('CommandFactory', function CommandFactory ($q, $http, $location) {
    'use strict';
    var exports = {};

    exports.fleets = [];
    exports.ships = [];
    exports.officers = [];
    exports.officer = [];

    exports.goToFleet = function(fleetId) {
      if ( angular.isNumber(fleetId) ) {
        $location.path('command/fleet/' + fleetId)
      }
    };

    exports.getFleets = function() {
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

    exports.getShips = function (fleetId) {
      var deferred = $q.defer();
      return $http.get('/api/ship/')
        .success(function (data) {
          exports.ships = getFleetShips(data, fleetId);
          exports.officers.length = 0;
          exports.officer.length = 0;
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

    exports.getOfficers = function (shipId) {
      var deferred = $q.defer();
      return $http.get('/api/officer/')
        .success(function (data) {
          exports.officers = getShipOfficers(data, shipId);
          console.log(exports.officers);
          exports.officer.length = 0;
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
        var officer = data[index];
        if (officer.ship == shipId) {
          officers.push(data[index]);
        }
      }
      return officers;
    }

    exports.getOfficer = function (officerId) {
      var deferred = $q.defer();
      return $http.get('/api/officer/' + officerId)
        .success(function (data) {
          exports.officer = [data];
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
