require 'src/Dependencies'

function love.load()
    math.randomseed(os.time())
    love.window.setTitle('Connect four!')
    love.graphics.setDefaultFilter('nearest', 'nearest')

    push:setupScreen(VIRTUAL_WIDTH, VIRTUAL_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT, {
        fullscreen = false,
        vsync = true,
        resizable = false
    })

    love.graphics.setFont(gFonts['small'])

    gStateMachine = StateMachine {
        ['start'] = function() return StartState() end,
        ['play'] = function() return PlayState() end,
        ['game-over'] = function() return GameOverState() end
    }
    gStateMachine:change('start')

    gSounds['music']:setLooping(true)
    gSounds['music']:play()

    love.keyboard.keysPressed = {}

    backgroundX1 = 0
    backgroundX2 = gTextures['background']:getWidth()
    backgroundX3 = backgroundX2 * 2
end

function love.resize(w, h)
    push:resize(w, h)
end

function love.keypressed(key)
    love.keyboard.keysPressed[key] = true
end

function love.keyboard.wasPressed(key)
    return love.keyboard.keysPressed[key]
end

function love.update(dt)

    backgroundX1 = backgroundX1 - BACKGROUNDSCROLLSPEED * dt
    backgroundX2 = backgroundX2 - BACKGROUNDSCROLLSPEED * dt
    backgroundX3 = backgroundX3 - BACKGROUNDSCROLLSPEED * dt

    if backgroundX1 <= -gTextures['background']:getWidth() then
        backgroundX1 = backgroundX3 + gTextures['background']:getWidth()
    elseif backgroundX2 <= -gTextures['background']:getWidth() then
        backgroundX2 = backgroundX1 + gTextures['background']:getWidth()
    elseif backgroundX3 <= -gTextures['background']:getWidth() then
        backgroundX3 = backgroundX2 + gTextures['background']:getWidth()
    end

    Timer.update(dt)
    gStateMachine:update(dt)

    love.keyboard.keysPressed = {}
end

function love.draw()
    push:start()

    love.graphics.draw(gTextures['background'], backgroundX3)
    love.graphics.draw(gTextures['background'], backgroundX2)
    love.graphics.draw(gTextures['background'], backgroundX1)
    
    gStateMachine:render()
    push:finish()
end