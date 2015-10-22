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

        this.goToFleet = function(fleetId) {
          CommandFactory.goToFleet(fleetId);
        };

        CommandFactory.getFleets()
          .then( angular.bind( this, function then() {
            this.fleets = CommandFactory.fleets;
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