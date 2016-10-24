/*
 * Game state
 * ==========
 *
 * A sample Game state, displaying the Phaser logo.
 */


export default class Game extends Phaser.State {

  create() {
    // TODO: Replace this with really cool game code here :)

    const {centerX: x, centerY: y} = this.world;
    this.createPlayer(x, y);
    this.createControls();

  }

  createPlayer(posX, posY) {
    var rectSize = { width: 50, height: 50 };

    this.player = this.add.graphics(posX, posY);

    this.player.drawRect(posX, posY, rectSize.width, rectSize.height);
    this.player.beginFill(0x00aaff, 1);
    this.player.endFill();

    this.game.physics.enable(this.player, Phaser.Physics.ARCADE);
  }

  createControls() {
    this.controls = this.input.keyboard.createCursorKeys();
  }

  // UPDATE
  update() {
    this.checkControls();
  }

  checkControls() {
    function move(obj, dirAxis, velocity) {
      console.log(dirAxis, ': ', obj[dirAxis]);
      obj.body.velocity[dirAxis] += velocity;
    }

    // Up and down
    if (this.controls.up.isDown) {
      move(this.player, 'y', -5);
    } else if (this.controls.down.isDown) {
      move(this.player, 'y', 5);
    }

    // Left and right
    if (this.controls.left.isDown) {
      move(this.player, 'x', -5);
    } else if (this.controls.right.isDown) {
      move(this.player, 'x', 5);
    }
  }

  // render() {
  //   this.game.debug.geom(this.player, '#00aaff');
  // }
}
