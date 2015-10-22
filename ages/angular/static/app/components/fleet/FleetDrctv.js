/**
 * Directive: Fleet <fleet></fleet>
 */
angular.module('GalacticApp')
  .directive('fleet', function FleetDrctv ($timeout) {
    'use strict';

    return {
      restrict: 'EA',
      replace: true,
      scope: true,
      templateUrl: "/static/app/components/fleet/fleet.tmpl.html",
      controllerAs: 'fleet',

      controller: function ($routeParams, FleetFactory) {
        this.ships = {};

        var fleetId = Number($routeParams.fleetId);

        this.goToShip = function(shipId) {
          FleetFactory.goToShip(fleetId, shipId);
        };

        this.goToCommand = function() {
          FleetFactory.goToCommand();
        };

        FleetFactory.getShips($routeParams.fleetId)
          .then( angular.bind( this, function then() {
            this.ships = FleetFactory.ships;
          }));
      },

      link: function(scope, element, attrs, ctrl) {
        /*
          by convention we do not $ prefix arguments to the link function
          this is to be explicit that they have a fixed order
        */
      }
    };


  });