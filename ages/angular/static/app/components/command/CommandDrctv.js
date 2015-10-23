/**
 * Directive: Command <command></command>
 */
angular.module('GalacticApp')
  .directive('command', function CommandDrctv ($timeout) {
    'use strict';

    return {
      restrict: 'EA',
      replace: true,
      scope: true,
      templateUrl: "/static/app/components/command/command.tmpl.html",
      controllerAs: 'command',

      controller: function (CommandFactory) {
        this.fleets = {};
        this.ships = {};
        this.officers = {};
        this.officer = {};

        CommandFactory.getFleets()
          .then( angular.bind( this, function then() {
            this.fleets = CommandFactory.fleets;
          }));

        this.getShips = function(fleetId) {
          CommandFactory.getShips(fleetId)
            .then( angular.bind(this, function then() {
              this.ships = CommandFactory.ships;
            }))
        };

        this.getOfficers = function(shipId) {
          CommandFactory.getOfficers(shipId)
            .then( angular.bind(this, function then() {
              this.officers = CommandFactory.officers;
            }))
        };

        this.getOfficer = function(officerId) {
          CommandFactory.getOfficer(officerId)
            .then( angular.bind(this, function then() {
              this.officer = CommandFactory.officer;
            }))
        };
      },

      link: function(scope, element, attrs, ctrl) {
        /*
          by convention we do not $ prefix arguments to the link function
          this is to be explicit that they have a fixed order
        */
      }
    };
  });