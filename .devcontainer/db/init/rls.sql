ALTER TABLE dat_todo ENABLE ROW LEVEL SECURITY;

CREATE POLICY user_can_select_own_rows
  ON dat_todo
  FOR SELECT, INSERT, UPDATE, DELETE
  USING (user_id = current_setting('app.current_user')::integer);
