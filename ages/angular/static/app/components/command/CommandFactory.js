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

    exports.getFleets = function() {
      var deferred = $q.defer();
      return $http.get('/api/fleet/')
        .success(function (data) {
          exports.fleets = data.sort(compareName);
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    exports.getShips = function (fleetId) {
      var deferred = $q.defer();
      return $http.get('/api/fleet-ships/' + fleetId + '/')
        .success(function (data) {
          exports.ships = data.sort(compareName);
          exports.officers.length = 0;
          exports.officer.length = 0;
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    exports.getOfficers = function (shipId) {
      var deferred = $q.defer();
      return $http.get('/api/ship-officers/' + shipId + '/')
        .success(function (data) {
          exports.officers = data.sort(compareName);
          exports.officer.length = 0;
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    exports.getOfficer = function (officerId) {
      var deferred = $q.defer();
      return $http.get('/api/officer/' + officerId + '/')
        .success(function (data) {
          exports.officer = [data];
          deferred.resolve(data);
        })
        .error(function (data) {
          deferred.reject(data);
        });
      return deferred.promise;
    };

    function compareName(a,b) {
      if (a.name < b.name)
        return -1;
      if (a.name > b.name)
        return 1;
      return 0;
    }

    return exports;
  });
