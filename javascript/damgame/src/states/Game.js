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

    this.player = this.add.sprite(0, 0);

    // var rect = this.add.graphics(rectSize.x, rectSize.y);
    var rect = this.add.graphics(this.width, this.height);
    rect.beginFill(0xffffff, 1);
    rect.x = 0;
    rect.y = 0;
    rect.drawRect(0, 0, rectSize.x, rectSize.y);

    this.player.width = rectSize.x;
    this.player.height = rectSize.y;
    this.player.addChild(rect);

    this.physics.enable(this.player, Phaser.Physics.ARCADE);

    window.graphics = rect;
  }

  createControls() {
    this.controls = this.input.keyboard.createCursorKeys();
  }

  // UPDATE
  update() {
    this.checkControls();
  }

  checkControls() {
    if (this.controls.up.isDown) {
      this.player.body.velocity.y -= 5;
    }
  }

  render() {
  }
}
