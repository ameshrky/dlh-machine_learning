-- Stored procedure that computes weighted average score for a user
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE weighted_avg FLOAT;

SELECT SUM(corrections.score * projects.weight) / SUM(projects.weight)
INTO weighted_avg
FROM corrections
INNER JOIN projects ON corrections.project_id = projects.id
WHERE corrections.user_id = user_id;

UPDATE users SET average_score = IFNULL(weighted_avg, 0) WHERE id = user_id;

END//
DELIMITER ;
