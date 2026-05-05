module Main where
-- PROJECT: Servant REST API | stack run or cabal run
-- Docs: https://docs.servant.dev/

-- TODO 1: Imports (add to .cabal file: servant-server, warp, aeson, data-default)
-- import Servant
-- import Network.Wai
-- import Network.Wai.Handler.Warp (run)
-- import Data.Aeson (FromJSON, ToJSON)
-- import GHC.Generics (Generic)

-- TODO 2: Data types with Aeson instances
-- data User = User { userId :: Int, userName :: String, userEmail :: String }
--   deriving (Generic, Show)
-- instance ToJSON User
-- instance FromJSON User
--
-- data CreateUserRequest = CreateUserRequest { reqName :: String, reqEmail :: String }
--   deriving (Generic, Show)
-- instance FromJSON CreateUserRequest

-- TODO 3: API type definition
-- type UserAPI =
--        "users" :> Get '[JSON] [User]
--   :<|> "users" :> Capture "id" Int :> Get '[JSON] User
--   :<|> "users" :> ReqBody '[JSON] CreateUserRequest :> Post '[JSON] User
--   :<|> "users" :> Capture "id" Int :> Delete '[JSON] NoContent

-- TODO 4: Server implementation
-- userAPI :: Proxy UserAPI
-- userAPI = Proxy
--
-- server :: IORef [User] -> Server UserAPI
-- server ref = getUsers :<|> getUser :<|> createUser :<|> deleteUser
--   where
--     getUsers = liftIO $ readIORef ref
--     getUser id = do
--       users <- liftIO $ readIORef ref
--       case find ((== id) . userId) users of
--         Nothing -> throwError err404 { errBody = "User not found" }
--         Just u  -> return u
--     createUser req = do
--       users <- liftIO $ readIORef ref
--       let newId = length users + 1
--           user = User newId (reqName req) (reqEmail req)
--       liftIO $ modifyIORef ref (user:)
--       return user
--     deleteUser id = do
--       liftIO $ modifyIORef ref (filter ((/= id) . userId))
--       return NoContent

-- TODO 5: Main entry point
-- main :: IO ()
-- main = do
--   ref <- newIORef []
--   putStrLn "Servant server running on port 8080"
--   run 8080 (serve userAPI (server ref))

main :: IO ()
main = putStrLn "TODO: install servant-server, warp, aeson, then implement"
