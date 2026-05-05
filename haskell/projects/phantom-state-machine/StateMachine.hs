module StateMachine where
-- PROJECT: Type-Safe State Machine with Phantom Types (Exclusive)
-- Invalid state transitions become compile-time type errors.

-- TODO 1: Define phantom type tags (no constructors — just type tags)
-- data Locked
-- data Unlocked
-- data Open     -- extend to 3-state machine

-- TODO 2: Door type parameterized by state
-- newtype Door s = Door { doorId :: Int } deriving (Show)
-- -- The 's' type parameter is "phantom" — it appears only in the type, not the value

-- TODO 3: Constructor — all doors start locked
-- create :: Int -> Door Locked
-- create = Door

-- TODO 4: State transitions — type signatures enforce valid transitions
-- unlock :: Door Locked -> String -> Either String (Door Unlocked)
-- unlock (Door id) key
--   | key == "secret" = Right (Door id)
--   | otherwise       = Left "Wrong key"
--
-- lock :: Door Unlocked -> Door Locked
-- lock (Door id) = Door id
--
-- open :: Door Unlocked -> Door Open
-- open (Door id) = Door id
--
-- close :: Door Open -> Door Unlocked
-- close (Door id) = Door id

-- TODO 5: Actions only valid in certain states
-- enter :: Door Open -> String
-- enter (Door id) = "Walking through door " ++ show id
--
-- insertKey :: Door Locked -> String -> String
-- insertKey (Door id) key = "Inserting key '" ++ key ++ "' into door " ++ show id

-- TODO 6: Prove invalid transitions fail to compile
-- badLock :: Door Locked -> Door Locked
-- badLock = lock   -- TYPE ERROR: lock :: Door Unlocked -> Door Locked
--
-- badEnter :: Door Locked -> String
-- badEnter = enter  -- TYPE ERROR: enter :: Door Open -> String

-- TODO 7: Traffic light — only valid transitions allowed
-- data RedLight
-- data GreenLight
-- data YellowLight
--
-- data Light s = Light deriving (Show)
--
-- red    :: Light RedLight
-- red    = Light
--
-- advance :: Light RedLight -> Light GreenLight
-- advance Light = Light
--
-- slow   :: Light GreenLight -> Light YellowLight
-- slow   Light = Light
--
-- stop   :: Light YellowLight -> Light RedLight
-- stop   Light = Light
--
-- -- advance (slow red) -- TYPE ERROR: slow :: Green -> Yellow, not Red -> Yellow

-- TODO 8: Test in GHCi
-- let myDoor = create 42
-- case unlock myDoor "secret" of
--   Left err   -> putStrLn $ "Error: " ++ err
--   Right door -> do
--     let opened = open door
--     putStrLn $ enter opened
--     let closed = close opened
--     let relocked = lock closed
--     putStrLn "Door is locked again"
